using Kasino.Models;

namespace Kasino.Repositories
{
  /// <summary>
  /// Interface for asynchronous operations on players.
  /// </summary>
  public interface IPlayerRepository
  {
    /// <summary>
    /// Get all players asynchronously.
    /// </summary>
    /// <returns>An enumerable collection of players.</returns>
    Task<IEnumerable<Player>> GetAllPlayersAsync();

    /// <summary>
    /// Get a player by ID asynchronously.
    /// </summary>
    /// <param name="id">The ID of the player to fetch.</param>
    /// <returns>The player with the specified ID.</returns>
    Task<Player> GetPlayerByIdAsync(string id);

    /// <summary>
    /// Add a new player asynchronously.
    /// </summary>
    /// <param name="player">The player to add.</param>
    Task CreatePlayerAsync(Player player);

    /// <summary>
    /// Update an existing player asynchronously.
    /// </summary>
    /// <param name="player">The player to update.</param>
    Task UpdatePlayerAsync(Player player);

    /// <summary>
    /// Remove a player asynchronously.
    /// </summary>
    /// <param name="player">The player to remove.</param>
    Task DeletePlayerAsync(Player player);

    /// <summary>
    /// Add a player asynchronously.
    /// </summary>
    /// <param name="player">The player to add.</param>
    Task AddPlayerAsync(Player player);
  }
}