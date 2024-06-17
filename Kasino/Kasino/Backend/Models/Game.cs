namespace Kasino.Models
{
  /*This code defines a Game class that represents a card game. It has properties for 
   * Id, Players, FloorCards, Deck, and CurrentRound. 
   * It also includes methods for dealing cards, capturing cards, building, trailing, and calculating scores in the game.*/
  public class Game
  {
    public string Id { get; set; }
    public List<Player> Players { get; set; } = new List<Player>();
    public List<Card> FloorCards { get; set; } = new List<Card>();
    public Deck Deck { get; set; } = new Deck();
    public int CurrentRound { get; set; }

    public void DealCards()
    {
      int cardsPerPlayer;
      int initialFloorCards;

      switch (Players.Count)
      {
        case 2:
          cardsPerPlayer = 10; // 2 rounds of 10 cards each
          initialFloorCards = 0; // No initial table cards for 2 players
          break;
        case 3:
          cardsPerPlayer = 13; // 13 cards per player
          initialFloorCards = 1; // 1 initial table card for 3 players
          break;
        case 4:
          cardsPerPlayer = 10; // 10 cards per player
          initialFloorCards = 0; // No initial table cards for 4 players
          break;
        default:
          throw new InvalidOperationException("Unsupported number of players");
      }

      // Deal cards to players
      foreach (var player in Players)
      {
        for (int i = 0; i < cardsPerPlayer; i++)
        {
          player.Hand.Add(Deck.DrawCard());
        }
      }

      // Place initial table cards
      for (int i = 0; i < initialFloorCards; i++)
      {
        FloorCards.Add(Deck.DrawCard());
      }
    }


    public void Capture(Card playedCard, Player player)
    {
      // Implement capture logic
    }

    public void Build(Card playedCard, Player player, int targetValue)
    {
      // Implement build logic
    }

    public void Trail(Card playedCard, Player player)
    {
      // Implement trailing logic
    }

    public void CalculateScores()
    {
      // Implement scoring logic
    }
  }
}