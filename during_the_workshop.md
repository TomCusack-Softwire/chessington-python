# Chessington

## The Brief

## Part 1

When you're ready, run the tests (with `poetry run pytest tests`). You'll notice you have some tests already - but some are failing! Run the unit tests and see what's failed. Working in a pair, implement the minimum functionality required to pass the tests.

When you've got that working, you can add new tests in using `git cherry-pick red-3` in a failing state. Again, implement the behaviour following TDD. Repeat this for red-4 and red-5, switching driver each time.

### Tips

* This is TDD, with someone else providing the tests.
* You won't need to make changes to the chessington/ui package (although feel free to explore it).
* Avoid print statements! If you need to debug an error, use the VSCode debugger.
* Use VSCode live share to work with your pair.

## Part 2 (stretch)

You've programmed Pawn movement, now for the rest of the pieces. We don't have any unit tests for these so you'll need to write them first.

For each of the following pieces, write unit tests and functionality following TDD. Make sure you follow the Red-Green-Refactor cycle! For this part, use ping-pong pairing. That means the driver writes a unit test, then the navigator makes it pass. Switch roles after every test.

1. King
2. Knight
3. Bishop
4. Rook
5. Queen

Stick to basic movement and capture tests. Don't worry about any of the more complex rules (check, checkmate, castling etc.) just yet.

## Part 3 (stretch)

Chessington can now play chess! But the game never ends, and it's missing some of the more situational rules. If you have time, work through the list of rules below using ping-pong pairing:

1. En Passant
2. Castling
3. Pawn Promotion
4. Check and Check Mate
5. Stalemate

Remember, only write code to make test cases pass. If you're not sure what these rules are, ask your pair or check online!
