// errorThrower.test.js
// contains a test that checks if the error is thrown correctly.
// Jest is used as the testing framework to run the test.

// When you run npm test, Jest will execute the test and confirm that the error handling works as expected.

const throwError = require('./errorThrower');

describe('Error Handling', () => {
    test('should handle the error gracefully', () => {
        const result = throwError();
        expect(result).toEqual({ success: false, message: "This is a test error" });
    });
});
