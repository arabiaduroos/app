import json
import re

with open('audio_index.json', 'r', encoding='utf-8') as f:
    audio_index = json.load(f)

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Prepare AUDIO_INDEX javascript string
audio_index_js = "  const AUDIO_INDEX = " + json.dumps(audio_index, ensure_ascii=False) + ";\n"

# 2. Upgraded speakArabic and fallbackTTS
audio_engine_js = """  // Arabic Audio Engine: Pre-synthesized studio-grade Male Voice (ar-SA-HamedNeural) + Dynamic Fallback
  let activeAudioTTS = null;

  function cleanArTextForAudio(text) {
    if (!text) return '';
    return text
      .replace(/\\[.*?\\]/g, '')
      .replace(/[\\(（][۰-۹0-9]+[\\)）]/g, '')
      .replace(/[•|⬅️➡️➔⬇️💡✨⭐\\?؟\\.,!:]/g, ' ')
      .replace(/\\s+/g, ' ')
      .trim();
  }

  function speakArabic(text) {
    if (!text) return;
    try {
      const clean = cleanArTextForAudio(text);
      if (!clean) return;

      // 1. Check if we have pre-rendered authentic Saudi Male voice (HamedNeural)
      let audioPath = AUDIO_INDEX[clean];
      if (!audioPath) {
        const bareClean = stripTashkeel(clean);
        for (const [key, path] of Object.entries(AUDIO_INDEX)) {
          if (stripTashkeel(key) === bareClean) {
            audioPath = path;
            break;
          }
        }
      }

      if (audioPath) {
        if (activeAudioTTS) {
          try {
            activeAudioTTS.pause();
            activeAudioTTS.currentTime = 0;
          } catch (e) {}
        }
        activeAudioTTS = new Audio(audioPath);
        activeAudioTTS.play().catch(e => {
          console.warn('Local audio play error, falling back to dynamic TTS:', e);
          fallbackTTS(clean);
        });
        return;
      }

      // 2. Fallback to Dynamic TTS (Male voice preference)
      fallbackTTS(clean);
    } catch (e) {
      console.warn('speakArabic error:', e);
    }
  }

  function fallbackTTS(clean) {
    let spokenLocal = false;
    if ('speechSynthesis' in window) {
      try {
        const voices = window.speechSynthesis.getVoices() || [];
        const arVoices = voices.filter(v => v.lang && v.lang.toLowerCase().startsWith('ar'));
        const maleVoice = arVoices.find(v => {
          const n = (v.name || '').toLowerCase();
          return n.includes('hamed') || n.includes('shakir') || n.includes('maged') ||
                 n.includes('taim') || n.includes('fahed') || n.includes('ali') ||
                 n.includes('bassel') || n.includes('omar') || n.includes('jamal') ||
                 n.includes('abdullah') || n.includes('moaz') || n.includes('male') ||
                 (v.gender && v.gender.toLowerCase() === 'male');
        }) || arVoices[0];

        if (maleVoice) {
          window.speechSynthesis.cancel();
          const utter = new SpeechSynthesisUtterance(clean);
          utter.lang = maleVoice.lang || 'ar-SA';
          utter.voice = maleVoice;
          utter.pitch = 0.82; // Resonant masculine teacher tone
          utter.rate = 0.88;
          window.speechSynthesis.speak(utter);
          spokenLocal = true;
        }
      } catch (err) {
        spokenLocal = false;
      }
    }

    if (!spokenLocal) {
      if (activeAudioTTS) {
        try {
          activeAudioTTS.pause();
          activeAudioTTS.currentTime = 0;
        } catch (e) {}
      }
      const encoded = encodeURIComponent(clean);
      const url = `https://translate.google.com/translate_tts?ie=UTF-8&tl=ar&client=tw-ob&q=${encoded}`;
      activeAudioTTS = new Audio(url);
      activeAudioTTS.play().catch(e => {
        console.warn('Cloud audio playback error:', e);
      });
    }
  }
"""

# Replace the existing speakArabic block
old_speak_pattern = re.compile(r'  // Arabic TTS: Dual Engine.*?\n  function getBook', re.DOTALL)
m = old_speak_pattern.search(code)
if m:
    replacement = audio_index_js + audio_engine_js + "\n  function getBook"
    code = code[:m.start()] + replacement + code[m.end()-len("  function getBook"):]
    print("1. Replaced speakArabic with Male Voice Audio Engine + AUDIO_INDEX")
else:
    print("Warning: old speakArabic pattern not matched!")

# Fix emojis in VOCAB_REGISTRY
code = code.replace("{ ar: 'خَفِيفٌ', ur: 'ہلکا', en: 'Light', emoji: '🪶' }", "{ ar: 'خَفِيفٌ', ur: 'ہلکا', en: 'Light', emoji: '🍃' }")
code = code.replace("{ ar: 'فَقِيرٌ', ur: 'غریب', en: 'Poor', emoji: '🪙' }", "{ ar: 'فَقِيرٌ', ur: 'غریب', en: 'Poor', emoji: '🤲' }")
print("2. Fixed emojis in VOCAB_REGISTRY (leaf 🍃, hands 🤲)")

# Also fix in DATA
code = code.replace('"emoji": "🪶"', '"emoji": "🍃"')
code = code.replace('"emoji": "🪙"', '"emoji": "🤲"')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Finished updating app.js!")
