using Kasino.Models;

namespace Kasino.Repositories
{
  public class PlayerRepository : IPlayerRepository
  {
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
