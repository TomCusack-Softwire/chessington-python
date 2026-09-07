# Chessington

Starter project for a chess-based TDD exercise.

Brief:

> We've started work on the Chessington app! The UX Team came up with a novel interface, and we've built the game engine and GUI. Problem is, Geoff is the only one who knows the rules of chess and he's gone for a really long lunch. We haven't been able to finish the job without him. That's where you come in.  
> Start with the simple pieces and we'll go from there. Management recently signed off a TDD approach so let's try that out. Work in pairs to keep that knowledge sharing up. Hopefully that'll reduce our dependence on Geoff in future…

Fork and clone this repo, then follow the instructions in [README.md](./README.md) to get the app and tests running.

**Make sure you copy all branches and tags, not just the master branch when you fork on GitHub.**

## Running the application

To run the application, first ensure that you have installed Poetry on your system. Install
dependencies using the command ``poetry install``.

To run the application, use the command ``poetry run start``. This will pop up a window containing
a chess board. Clicking on one of the white pieces will highlight the square that piece is on,
and also show you the squares it can move to. Except...

None of the rules of chess have been implemented yet! That's your job :)

## Running the tests

To run the tests, use the command `poetry run pytest tests`. This will search the "tests" directory for files starting in `test_` or ending in `_test`. Inside those files, any function starting with `test_` will be considered a test.

## Debugging

VSCode debug config has been set up, but you will need to select your virtual environments python interpreter
before running either the tests or app in debug mode. You can do this in VS Code by going to `View`->`Command Palette`,
searching for `Python: Select Interpreter` and then browse your machine to find the appropriate python executable
(e.g. `.venv\Scripts\python.exe` or `.venv\Scripts\python`)

## GUI Dependencies

The application runs a desktop GUI using Tkinter. If you're running an official Python distribution, this will just
work out of the box.

Users relying on third-party Python installations (e.g. Mac/Linux system installs, package managers) may need to configure
Tcl/Tk separately, or download an official Python distribution for use on this codebase.

Mac users can check out <https://www.python.org/download/mac/tcltk/> for further details.


# Guide to the code

## Board

