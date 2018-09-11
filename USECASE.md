[Use Case: Tic-Tac-Toe](#Use-Case-Tic-Tac-Toe)

---

#### Use Case Tic-Tac-Toe

A fully executed contract should define the overall desired state.

In a game of tic-tac-toe an empty board represents the initial state of the contract.


|    | 0  | 1  | 2  |
|----|----|----|----|
|  0 |    |    |    |
|  1 |    |    |    |
|  2 |    |    |    |



In the diagram above observe that we have added a numbering schema to define possible moves of the game.

---

Each input into the contract can be thought of as the occurrence of an event.

In tic-tac-toe PlayerX goes first, but before that we can consider that 
the two players must have arranged to play a game.

We can model this as a 'Begin' event where PlayerX and PlayerO have agreed to play a game.

---

Here's an example of a sequence of events for a completed game using a simple time index to order the events.

Time 0: GameBegin(PlayerX, PlayerO)

Player X makes the first move of the game.
Time 1: Move(X, 11)

Followed by PlayerO
Time 2: Move(O, 02)

    ┌───┬───┬───┐
    │ - │ - │ O │
    ├───┼───┼───┤
    │ - │ X │ - │
    ├───┼───┼───┤
    │ - │ - │ - │
    └───┴───┴───┘

Here is what a snapshot of the board now looks like.

Gameplay continues...

Time 3: Move(X, 22)
Time 4: Move(O, 00)
Time 5: Move(X, 01)
Time 6: Move(O, 10)
Time 7: Move(X, 21)
Time 8: GameOver(Win, PlayerX)

    ┌───┬───┬───┐
    │ O │ X │ O │
    ├───┼───┼───┤
    │ O │ X │ - │
    ├───┼───┼───┤
    │ - │ X │ X │
    └───┴───┴───┘

Above is the final view of the board.
Notice that the empty spaces are now disabled because the game has terminated.
