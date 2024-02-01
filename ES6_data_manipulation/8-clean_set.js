export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') {
    return '';
  }
  const cleanedSet = [];
  for (const word of set) {
    if (word && word.startsWith(startString)) {
      cleanedSet.push(word.replace(startString, ''));
    }
  }
  return cleanedSet.join('-');
}
