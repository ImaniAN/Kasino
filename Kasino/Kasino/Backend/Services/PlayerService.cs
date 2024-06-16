using Kasino.Models;
using Kasino.Repositories;

namespace Kasino.Services
{
  public class PlayerService : IPlayerService
  {
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