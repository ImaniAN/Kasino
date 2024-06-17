using Kasino.Data;
using Kasino.Models;

namespace Kasino.Repositories
{
  public class PlayerRepository : IPlayerRepository
  {  /*This code defines a PlayerRepository class that implements the IPlayerRepository interface. 
      * It interacts with a GameDbContext to perform asynchronous operations for 
      * getting all players, fetching a player by ID, and creating a new player. 
      * Additional methods for updating and deleting players can be added.*/

    private readonly GameDbContext _context;

    public PlayerRepository(GameDbContext context)
    {
      _context = context;
    }

    public async Task<IEnumerable<Player>> GetAllPlayersAsync()
    {
      return await _context.Players.ToListAsync();
    }

    public async Task<Player> GetPlayerByIdAsync(string id)
    {
      return await _context.Players.FindAsync(id);
    }

    public async Task CreatePlayerAsync(Player player)
    {
      _context.Players.Add(player);
      await _context.SaveChangesAsync();
    }

    // Additional methods for update, delete
  }
}