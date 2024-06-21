namespace Kasino.Backend.DTOs
{
  public class GameSessionDto
  {
    // Unique identifier for the game session
    public string? SessionId { get; set; }

    // List of players participating in this game session
    public List<PlayerDto> Players { get; set; } = new List<PlayerDto>();

    // Current state of the game (e.g., "WaitingForPlayers", "InProgress", "Completed")
    public string? GameState { get; set; }

    // Scores or other metrics relevant to the game's outcome
    public Dictionary<string, int> Scores { get; set; } = new Dictionary<string, int>();

    // Timestamp for when the game session started
    public DateTime StartTime { get; set; }

    // Timestamp for when the game session ended (if it has ended)
    public DateTime? EndTime { get; set; }

    // Additional properties or methods as needed for managing game sessions
  }
}