using Kasino.Models;
using Kasino.Repositories;

namespace Kasino.Services
{
  /// <summary>
  /// Service for managing player data
  /// </summary>
  public class PlayerService : IPlayerService
  {
    private readonly IPlayerRepository _playerRepository;

    /// <summary>
    /// Constructor for PlayerService
    /// </summary>
    /// <param name="playerRepository">Player repository dependency</param>
    public PlayerService(IPlayerRepository playerRepository)
    {
      _playerRepository = playerRepository;
    }

    /// <summary>
    /// Get all players asynchronously
    /// </summary>
    /// <returns>The list of all players</returns>
    public async Task<IEnumerable<Player>> GetAllPlayersAsync()
    {
      return await _playerRepository.GetAllPlayersAsync();
    }

    /// <summary>
    /// Get a player by ID asynchronously
    /// </summary>
    /// <param name="id">Player ID</param>
    /// <returns>The player with the specified ID</returns>
    public async Task<Player> GetPlayerByIdAsync(string id)
    {
      return await _playerRepository.GetPlayerByIdAsync(id);
    }

    /// <summary>
    /// Update a player's score asynchronously
    /// </summary>
    /// <param name="id">Player ID</param>
    /// <param name="newScore">New score to set</param>
    /// <returns>True if the update was successful, false otherwise</returns>
    public async Task<bool> UpdatePlayerScoreAsync(string id, int newScore)
    {
      var player = await _playerRepository.GetPlayerByIdAsync(id);
      if (player == null)
      {
        return false;
      }

      player.Score = newScore;
      await _playerRepository.UpdatePlayerAsync(player);
      return true;
    }

    /// <summary>
    /// Delete a player by ID asynchronously
    /// </summary>
    /// <param name="id">Player ID</param>
    /// <returns>True if the deletion was successful, false otherwise</returns>
    public async Task<bool> DeletePlayerAsync(string id)
    {
      var player = await _playerRepository.GetPlayerByIdAsync(id);
      if (player == null)
      {
        return false;
      }

      await _playerRepository.DeletePlayerAsync(player);
      return true;
    }

    /// <summary>
    /// Create a new player asynchronously
    /// </summary>
    /// <param name="player">Player object to create</param>
    /// <returns>The created player</returns>
    public async Task<Player> CreatePlayerAsync(Player player)
    {
      await _playerRepository.AddPlayerAsync(player);
      return player;
    }
  }
}
