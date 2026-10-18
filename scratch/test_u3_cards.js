const fs = require('fs');

const code = fs.readFileSync('app.js', 'utf8');
const dataCode = fs.readFileSync('data/madinah_books.js', 'utf8');

// Evaluate in sandbox
const vm = require('vm');
const context = {
  window: {},
  document: {
    readyState: 'complete',
    getElementById: () => ({ addEventListener: () => {}, classList: { add: () => {}, remove: () => {}, toggle: () => {} }, style: {} }),
    querySelectorAll: () => [],
    querySelector: () => null
  },
  localStorage: { getItem: () => null, setItem: () => {} }
};
vm.createContext(context);
vm.runInContext(dataCode, context);
vm.runInContext(code, context);

const u3 = context.window.MADINAH_BOOKS.books[0].units[2];
console.log('Unit 3 title:', u3.title_ar);
console.log('Flow items:', u3.curriculum_flow.length);
console.log('Questions:', u3.questions.length);

const cards = context.window.app.openLessonCardReader ? [] : [];
// Let's call openLessonCardReader(u3)
context.window.app.openLessonCardReader(u3);
// Access lessonReader cards
// We can check how many cards were generated
console.log('Cards in lessonReader:');
// Let's check context.window.app
