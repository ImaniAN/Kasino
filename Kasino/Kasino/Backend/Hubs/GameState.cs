using Kasino.Models;

namespace Kasino.Backend.Hubs
{
  public class GameState
  {
    private readonly List<Move> moves = new List<Move>();
    private int lastMoveSequence = 0; // Tracks the last move sequence number

    public void AddMove(Move move)
    {
      // Increment the move sequence for each new move
      move.MoveSequence = ++lastMoveSequence;

      // Add the move to the list of moves
      moves.Add(move);

      // Points calculation and other game state updates should be handled separately
    }

    // This method should be called at the end of the game to calculate points for each player
    public int CalculatePoints(List<Card> playerCards)
    {
      int points = 0;

      // Utilize the PointValue method from the Card class for special cards
      points += playerCards.Sum(card => card.PointValue());

      // Card count points
      if (playerCards.Count == 20) points += 1;
      else if (playerCards.Count > 20) points += 2;

      // Spades count points
      int spadesCount = playerCards.Count(card => card.Suit == Suits.S);
      if (spadesCount >= 5) points += 1;

      // Adjust the logic to use the enums correctly and utilize the Card class methods
      // Note: The logic for Ten of Diamonds, Two of Spades, and Aces is now handled by card.PointValue()

      return points;
    }
  }
}
