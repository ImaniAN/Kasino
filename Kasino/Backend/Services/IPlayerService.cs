using Kasino.Models;

namespace Kasino.Services
{
  /// <summary>
  /// Interface for interacting with player data asynchronously.
  /// </summary>
  public interface IPlayerService
  {
    /// <summary>
    /// Fetches all players asynchronously.
    /// </summary>
    Task<IEnumerable<Player>> GetAllPlayersAsync();

    /// <summary>
    /// Fetches a player by ID asynchronously.
    /// </summary>
    Task<Player> GetPlayerByIdAsync(string id);

    /// <summary>
    /// Updates a player's score asynchronously.
    /// </summary>
    Task<bool> UpdatePlayerScoreAsync(string id, int newScore);

    /// <summary>
    /// Deletes a player asynchronously.
    /// </summary>
    Task<bool> DeletePlayerAsync(string id);

    /// <summary>
    /// Adds a new player asynchronously and returns the created player object or its identifier.
    /// </summary>
    Task<Player> CreatePlayerAsync(Player player);
  }
}