public class PlayerDTO
{/*This code defines a data transfer object (DTO) for a player. 
  * It contains properties for 
  * PlayerId, Name, Score, and a list of GameDTO's representing games associated with the player.

*/
  public string PlayerId { get; set; }
  public string Name { get; set; }
  public int Score { get; set; }
  public List<GameDTO> Games { get; set; } = new List<GameDTO>();

  // Additional properties or methods as needed for data transfer
}

