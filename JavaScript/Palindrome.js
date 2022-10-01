const isPalindrome = (str) => {
  if (typeof str !== 'string') {
    return 'Input must be string';
  }

  const len = str.length;

  for (let i = 0; i < len / 2; i++) {
    if (str[i] !== str[len - 1 - i]) {
      return `${str} is not a palindrome`;
    }
  }
  return `${str} is a palindrome`;
};

console.log(isPalindrome('ababa'));
console.log(isPalindrome('abcde'));
