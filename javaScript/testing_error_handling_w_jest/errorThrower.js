// errorThrower.js
// contains a function that throws an error

function throwError() {
    try {
        // Simulate an operation that throws an error
        throw new Error("This is a test error");
    } catch (error) {
        // Handle the error gracefully
        console.error("An error occurred:", error.message);
        return { success: false, message: error.message };
    }
}

module.exports = throwError;
