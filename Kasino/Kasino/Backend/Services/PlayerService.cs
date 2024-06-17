using Kasino.Models;
using Kasino.Repositories;

namespace Kasino.Services
{
  public class PlayerService : IPlayerService
  {/*This code defines a PlayerService class that implements the IPlayerService interface. 
    * It interacts with a IPlayerRepository to perform operations like 
    * getting all players, 
    * fetching a player by ID,
    * updating a player's score, 
    * deleting a player, 
    * and creating a new player with asynchronous methods.*/
    private readonly IPlayerRepository _playerRepository;

    public PlayerService(IPlayerRepository playerRepository)
    {
      _playerRepository = playerRepository;
    }

    public async Task<IEnumerable<Player>> GetAllPlayersAsync()
    {
      return await _playerRepository.GetAllPlayersAsync();
    }

    public async Task<Player> GetPlayerByIdAsync(string id)
    {
      return await _playerRepository.GetPlayerByIdAsync(id);
    }

    // New method to update a player's score
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

    // New method to delete a player
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

    public Task CreatePlayerAsync(Player player)
    {
      throw new NotImplementedException();
    }
  }
}
