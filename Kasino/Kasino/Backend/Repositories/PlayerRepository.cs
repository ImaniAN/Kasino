using Kasino.Data;
using Kasino.Models;
using System.Data.Entity;

namespace Kasino.Repositories
{
  // PlayerRepository handles database operations for Player entities
  public class PlayerRepository
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
    public async Task<Player> GetPlayerByIdAsync(int id)
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
      var existingPlayer = await _context.Players.FindAsync(player.Id);
      if (existingPlayer != null)
      {
        // Update each property manually
        existingPlayer.Name = player.Name;
        existingPlayer.Score = player.Score;

        // Save changes
        await _context.SaveChangesAsync();
      }
    }

    // Delete a player asynchronously
    public async Task DeletePlayerAsync(Player player)
    {
      var existingPlayer = await _context.Players.FindAsync(player.Id);
      if (existingPlayer != null)
      {
        _context.Players.Remove(existingPlayer);
        await _context.SaveChangesAsync();
      }
    }
  }
}
