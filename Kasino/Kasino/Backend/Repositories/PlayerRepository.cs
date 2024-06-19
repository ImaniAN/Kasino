using Kasino.Data;
using Kasino.Models;
using System.Data.Entity;

namespace Kasino.Repositories
{
  // PlayerRepository handles database operations for Player entities
  public class PlayerRepository : IPlayerRepository
  {
    private readonly GameDbContext _context;

    // Constructor for PlayerRepository
    public PlayerRepository(GameDbContext context)
    {
      _context = context;
    }

    // Get all players asynchronously
    public async Task<IEnumerable<Player>> GetAllPlayersAsync()
    {
      return await _context.Players.ToListAsync();
    }

    // Get a player by id asynchronously
    public async Task<Player> GetPlayerByIdAsync(string id)
    {
      return await _context.Players.FindAsync(id);
    }

    // Add a player asynchronously
    public async Task AddPlayerAsync(Player player)
    {
      _context.Players.Add(player);
      await _context.SaveChangesAsync();
    }

    // Create a player asynchronously, similar to AddPlayerAsync
    public async Task<Player> CreatePlayerAsync(Player player)
    {
      _context.Players.Add(player);
      await _context.SaveChangesAsync();
      return player;
    }

    // Update a player asynchronously
    public async Task UpdatePlayerAsync(Player player)
    {
      _context.Entry(player).State = EntityState.Modified;
      await _context.SaveChangesAsync();
    }

    // Delete a player asynchronously
    public async Task DeletePlayerAsync(Player player)
    {
      if (_context.Entry(player).State == EntityState.Detached)
      {
        _context.Players.Attach(player);
      }
      _context.Players.Remove(player);
      await _context.SaveChangesAsync();
    }
  }
}
