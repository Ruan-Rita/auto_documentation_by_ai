# Technical Documentation: LogService

## Overview

The `LogService` class provides a simple logging mechanism for a Node.js application. It allows writing log messages and error messages to separate files. The service creates a log directory if it doesn't exist and appends messages to the specified log files, including a timestamp for each entry.

## 1. Class: `LogService`

### Description

The `LogService` class encapsulates the functionality for writing log and error messages to files.

### Attributes

*   `directory`: (string) The directory where log files are stored (default: `'./src/logs/'`).
*   `loggFile`: (string) The name of the log file for general log messages (default: `'nodejs.log'`).
*   `errorFile`: (string) The name of the log file for error messages (default: `'error.log'`).

### Constructor

The constructor initializes the log directory. If the directory doesn't exist, it creates one.

## 2. Methods

### `logg(fileContent)`

Writes a log message to the `loggFile`.

*   `fileContent`: (any) The content to be logged (will be stringified).
*   It prepends the current date and time to the log message.
*   Uses `addContent` method to append the formatted log message to the log file.

### `error(fileContent)`

Writes an error message to the `errorFile`.

*   `fileContent`: (any) The content to be logged (will be stringified).
*   It prepends the current date and time to the error message.
*   Uses `addContent` method to append the formatted error message to the error file.

### `addContent(filePath, fileContent)`

Appends the given content to the specified file.

*   `filePath`: (string) The path to the file.
*   `fileContent`: (string) The content to append to the file.
*   It adds a newline character `\n` after the content.
*   Handles potential errors during file appending, logging any errors to the console.

## 3. Dependencies

*   `fs` (Node.js File System module): Used for file system operations like checking if a directory exists, creating a directory, and appending to a file.
*   `path` (Node.js Path module): Used for joining directory and file names to create file paths.
*    `formatDate` (from `../utils/date`): Used to format the current date and time for inclusion in the log messages.

## 4. File Structure

The service writes logs to files within a specified directory. The default directory is `./src/logs/`, and it contains two files:
*   `nodejs.log`: for standard logs
*   `error.log`: for errors

## 5. Usage

To use the `LogService`, you need to:

1.  Import the `LogService` class.
2.  Create an instance of the `LogService`.
3.  Call the `logg()` method to write log messages or the `error()` method to write error messages.

## 6. Error Handling

The `addContent` method includes basic error handling for file appending operations. If an error occurs during the `fs.appendFile` operation, it logs the error message to the console.

## 7. Date Formatting

The `formatDate` function (imported from `'../utils/date'`) is used to format the date and time for log entries.  The specific implementation of `formatDate` is assumed to be available in the specified utility file.

## 8. Initialization

The constructor ensures that the log directory exists. If the directory does not exist, it creates one using `fs.mkdirSync`.

## 9. Modularization

The class is exported as a module, allowing it to be easily imported and used in other parts of the application via `module.exports = LogService;`.

## 10. Potential Improvements

*   Implement more robust error handling, including logging errors to a separate error stream or file.
*   Add support for different log levels (e.g., DEBUG, INFO, WARN, ERROR).
*   Implement log rotation to prevent log files from growing too large.
*   Add configuration options for the log directory and file names.