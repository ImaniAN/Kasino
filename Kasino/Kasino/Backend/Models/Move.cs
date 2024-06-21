namespace Kasino.Models
{
  public class Move
  {
    public Player Player { get; set; }
    public Card PlayedCard { get; set; }
    public MoveActionType ActionType { get; set; }
    public List<Card> TargetCards { get; set; } = new List<Card>(); // For Capture and Build actions
    public int TargetValue { get; set; } // For Build actions
    public int MoveId { get; set; } // Unique identifier for the move
    public string? PlayerId { get; set; } // Identifier of the player who made the move
    public List<Card> CardsPlayed { get; set; } = new List<Card>(); // Cards involved in the move
    public int MoveSequence { get; set; } // The sequence number of the move in the game
    public int PointsGained { get; set; } // Points gained from this move
    public DateTime Timestamp { get; set; }

    public enum MoveActionType
    {
      Capture,
      Build,
      Lahla,
      // Add more action types as needed
    }

    // Constructor for a simple move with no target cards or value
    public Move(Player player, Card playedCard, MoveActionType actionType)
    {
      Player = player;
      PlayedCard = playedCard;
      ActionType = actionType;
      PlayerId = player.Id; // Assuming Player class has an Id property
      CardsPlayed = new List<Card> { playedCard }; // Initialize with playedCard
                                                   // MoveSequence, PointsGained should be set elsewhere as they are not available here
      Timestamp = DateTime.UtcNow; // Capture the current time when the move is made
    }

    // Constructor for a move with target cards (e.g., capturing or building)
    public Move(Player player, Card playedCard, MoveActionType actionType, List<Card> targetCards)
        : this(player, playedCard, actionType)
    {
      TargetCards = targetCards;
    }

    // Constructor for a build move that requires a target value
    public Move(Player player, Card playedCard, MoveActionType actionType, int targetValue)
        : this(player, playedCard, actionType)
    {
      TargetValue = targetValue;
    }
  }
}