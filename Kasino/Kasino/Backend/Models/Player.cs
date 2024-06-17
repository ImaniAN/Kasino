namespace Kasino.Models
{  /*This code defines a C# class named Player with properties for player information such as 
    * Id, Name, Hand (a list of cards), CapturedCards (a list of cards), and Score. 
    * The properties have appropriate data types and some are initialized with default values.*/

  public class Player
  {
    public string? Id { get; set; }
    public string? Name { get; set; }
    public List<Card> Hand { get; set; } = new List<Card>();
    public List<Card> CapturedCards { get; set; } = new List<Card>();
    public int Score { get; set; }
  }
}