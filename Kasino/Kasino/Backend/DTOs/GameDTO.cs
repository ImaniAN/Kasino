public class GameDTO
{
  /*This code defines a data transfer object (DTO) for a game.
   * It contains properties for the game's Id, Name, Genre, and ReleaseDate, 
   * along with any additional properties relevant to the game's data transfer needs.*/
  public string Id { get; set; }
  public string Name { get; set; }
  public string Genre { get; set; }
  public DateTime ReleaseDate { get; set; }

  // Additional properties relevant to the game's data transfer needs
}

