namespace Kasino.Models
{
  public class Move
  {
    public Player Player { get; set; }
    public Card PlayedCard { get; set; }
    public MoveActionType ActionType { get; set; }
    public List<Card> TargetCards { get; set; } = new List<Card>(); // For Capture and Build actions
    public int TargetValue { get; set; } // For Build actions

    // Renamed ActionType enum to MoveActionType
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
