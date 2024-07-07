namespace Kasino.Backend.DTOs
{
  public class PlayersDto
  {/*This code defines a data transfer object (DTO) for a player.
  * It contains properties for
  * PlayerId, Name, Score, and a list of GameDTO's representing games associated with the player.

*/
    public string? PlayerId { get; set; }
    public string? Name { get; set; }
    public int Score { get; set; }
    public List<GameDto> Games { get; set; } = new List<GameDto>();

    // Additional properties or methods as needed for data transfer
  }
}