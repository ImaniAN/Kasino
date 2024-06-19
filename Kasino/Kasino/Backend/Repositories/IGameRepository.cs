using Kasino.Models;

namespace Kasino.Repositories
{
  /// <summary>
  /// Interface for interacting with game data asynchronously.
  /// </summary>
  public interface IGameRepository
  {
    /// <summary>
    /// Get all games asynchronously
    /// </summary>
    /// <returns>The list of all games</returns>
    Task<IEnumerable<Game>> GetAllGamesAsync();

    /// <summary>
    /// Get a game by ID asynchronously
    /// </summary>
    /// <param name="id">Game ID</param>
    /// <returns>The game with the specified ID</returns>
    Task<Game> GetGameByIdAsync(string id);

    /// <summary>
    /// Create a new game asynchronously
    /// </summary>
    /// <param name="game">Game object to create</param>
    Task CreateGameAsync(Game game);

    // Additional methods for update, delete
  }
}