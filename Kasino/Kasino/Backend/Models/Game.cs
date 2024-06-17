namespace Kasino.Models
{
  /*This code defines a Game class that represents a card game. It has properties for 
   * Id, Players, FloorCards, Deck, and CurrentRound. 
   * It also includes methods for dealing cards, capturing cards, building, Lahlaring, and calculating scores in the game.*/
  public class Game
  {
    public string Id { get; set; }
    public List<Player> Players { get; set; } = new List<Player>();
    public List<Card> FloorCards { get; set; } = new List<Card>();
    public Deck Deck { get; set; } = new Deck();
    public int CurrentRound { get; set; }

    // Method to check if a card is special based on more complex criteria
    public static bool IsCardSpecial(Card card)
    {
      // Example logic: A card is special if it's an Ace or Jack
      return card.Value == 1 || card.Value == 11;
    }

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
      // List to hold potential build cards from the floor
      List<Card> potentialBuildCards = new List<Card>();

      // Check if there are combinations on the floor that sum up to the target value
      foreach (var floorCard in FloorCards)
      {
        // This is a simplified check; in a real game, you'd need to check all combinations
        if (playedCard.Value + floorCard.Value == targetValue)
        {
          potentialBuildCards.Add(floorCard);
        }
      }

      // If a valid build is possible
      if (potentialBuildCards.Any())
      {
        // Create a new Build object (assuming you have such a class to represent builds)
        // This object would include the cards in the build and the player who created it
        // Create a new Build object with the 'owner' parameter provided
        Build newBuild = new Build(player, new List<Card> { playedCard }.Concat(potentialBuildCards).ToList());
        {
          Owner = player,
          Cards = new List<Card> { playedCard }.Concat(potentialBuildCards).ToList()
        };

        // Remove the played card from the player's hand
        player.Hand.Remove(playedCard);

        // Remove the used floor cards
        foreach (var card in potentialBuildCards)
        {
          FloorCards.Remove(card);
        }

        // Add the new build to the floor
        // Assuming FloorCards can also hold Build objects; you might need a separate collection for builds
        FloorCards.Add(newBuild);

        // Note: This example assumes a lot about the data structures you're using.
        // You'll need to adjust it to fit your actual class designs.
      }
      else
      {
        // Handle the case where a build is not possible
        // For example, you might throw an exception or simply return
        throw new InvalidOperationException("Build is not possible with the provided card and target value.");
      }
    }


    public void Lahla(Card playedCard, Player player)
    {
      // Check if Lahlaring is allowed based on game rules
      // For example, in some in 2 player 1st round, Lahlaring might is not allowed if the player can capture
      // This example does not include such logic for simplicity

      // Remove the played card from the player's hand
      player.Hand.Remove(playedCard);

      // Add the played card to the floor
      FloorCards.Add(playedCard);

      // Additional logic for special Lahlaring rules or effects might go here
    }


    public void CalculateScores()
    {
      foreach (var player in Players)
      {
        int score = 0;

        // Basic scoring: 1 point per captured card
        score += player.CapturedCards.Count;

        // Example of additional scoring rules
        // Award extra points for specific cards or combinations
        // This is highly dependent on your game's rules
        var specialCards = player.CapturedCards.Where(card => IsCardSpecial(card));
        score += specialCards.Count() * 2; // Example: Special cards are worth double points

        // Update the player's score
        player.Score += score; // Assuming Player has a Score property

        // Additional scoring logic here
        // For example, bonus points for capturing the most cards, specific combinations, etc.
      }

      // After calculating scores, you might want to determine the round or game winner
      // and perform any necessary game state updates
    }

  }
}