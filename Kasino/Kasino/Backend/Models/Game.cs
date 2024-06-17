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
        case 2 or 4:
          cardsPerPlayer = 10;
          initialFloorCards = 0;
          break;
        case 3:
          cardsPerPlayer = 13; // 13 cards per player
          initialFloorCards = 1; // 1 initial table card for 3 players
          break;
        default:
          throw new InvalidOperationException("Unsupported number of players");
      }

      // Deal cards to players
      foreach (var player in Players)
      {
        for (int i = 0; i < cardsPerPlayer; i++)
        {
          player.Hand.Add(Deck.DishCard());
        }
      }

      // Place initial table cards
      for (int i = 0; i < initialFloorCards; i++)
      {
        FloorCards.Add(Deck.DishCard());
      }
    }


    public void Capture(Card playedCard, Player player)
    {
      // List to hold cards to be captured from the floor
      List<Card> capturedCards = new List<Card>();

      // Check if the played card can directly capture any floor card
      foreach (var floorCard in FloorCards)
      {
        if (playedCard.Value == floorCard.Value)
        {
          capturedCards.Add(floorCard);
        }
      }

      // If direct capture is not possible, check for combinations that sum up to the played card's value
      // This part can get complex depending on the rules for combinations
      // For simplicity, this example does not include combination logic

      // Remove captured cards from the floor and add them to the player's CapturedCards
      foreach (var card in capturedCards)
      {
        FloorCards.Remove(card);
        player.CapturedCards.Add(card); // Assuming each player has a 'CapturedCards' to store captured cards
      }

      // Also add the played card to the player's CapturedCards
      player.CapturedCards.Add(playedCard);

      // Additional logic for special captures or scoring might go here
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