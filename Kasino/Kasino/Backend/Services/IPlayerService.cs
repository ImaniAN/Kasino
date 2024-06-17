using Kasino.Models;

namespace Kasino.Services
{
  public interface IPlayerService
  {/*This code snippet defines an interface IPlayerService with methods to interact with player data asynchronously. 
    * The methods include fetching all players, getting a player by ID, updating a player's score, and deleting a player.*/
    Task<IEnumerable<Player>> GetAllPlayersAsync();
    Task<Player> GetPlayerByIdAsync(string id);
    Task<bool> UpdatePlayerScoreAsync(string id, int newScore);
    Task<bool> DeletePlayerAsync(string id);
    // Adds a new player asynchronously and returns the created player object or its identifier
    Task<Player> CreatePlayerAsync(Player player);
  }
}
