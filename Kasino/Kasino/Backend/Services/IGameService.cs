
using Kasino.Models;

namespace Kasino.Backend.Services
{
  /// <summary>
  /// Interface for game service operations.
  /// </summary>
  public interface IGameService
  {
    /// <summary>
    /// Asynchronously creates a new game.
    /// </summary>
    /// <param name="game">The game to create.</param>
    Task CreateGameAsync(Game game);

    /// <summary>
    /// Asynchronously retrieves all games.
    /// </summary>
    Task<object?> GetAllGamesAsync();

    /// <summary>
    /// Asynchronously retrieves a game by its ID.
    /// </summary>
    /// <param name="id">The ID of the game to retrieve.</param>
    Task<Game> GetGameByIdAsync(string id);
  }
}