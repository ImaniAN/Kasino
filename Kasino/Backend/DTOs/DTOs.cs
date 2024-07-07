namespace Kasino.Backend.DTOs
{
  public record PlayerDto(string? PlayerId, string? Name, int Score)
  {
    public List<GameDto> Games { get; set; } = new List<GameDto>();

    // Constructor to initialize all properties, including Games
    public PlayerDto(string? playerId, string? name, int score, List<GameDto> games) : this(playerId, name, score)
    {
      Games = games;
    }

    // Additional properties or methods as needed for data transfer
  }

  public class GameDto
  {
    /* This code defines a data transfer object (DTO) for a game.
     * It contains properties for the game's Id, Name, and additional properties
     * relevant to the game's data transfer needs.
     */
    public string? Id { get; set; }
    public string? Name { get; set; }
    public string? Genre { get; set; }
    public DateTime ReleaseDate { get; set; }

    // Additional properties or methods as needed for data transfer
  }
}