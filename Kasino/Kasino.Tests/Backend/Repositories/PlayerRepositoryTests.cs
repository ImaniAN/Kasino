namespace Kasino.Tests.Repositories
{
  using System;
  using System.Threading.Tasks;
  using Kasino.Data;
  using Kasino.Models;
  using Kasino.Repositories;
  using Xunit;

  public class PlayerRepositoryTests
  {
    private PlayerRepository _testClass;
    private GameDbContext _context;

    public PlayerRepositoryTests()
    {
      _context = new GameDbContext(new DbContextOptions<GameDbContext>());
      _testClass = new PlayerRepository(_context);
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new PlayerRepository(_context);

      // Assert
      Assert.NotNull(instance);
    }

    [Fact]
    public void CannotConstructWithNullContext()
    {
      Assert.Throws<ArgumentNullException>(() => new PlayerRepository(default(GameDbContext)));
    }

    [Fact]
    public async Task CanCallGetAllPlayersAsync()
    {
      // Act
      var result = await _testClass.GetAllPlayersAsync();

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CanCallGetPlayerByIdAsync()
    {
      // Arrange
      var id = 521554362;

      // Act
      var result = await _testClass.GetPlayerByIdAsync(id);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task GetPlayerByIdAsyncPerformsMapping()
    {
      // Arrange
      var id = 1392289794;

      // Act
      var result = await _testClass.GetPlayerByIdAsync(id);

      // Assert
      Assert.Same(id, result.Id);
    }

    [Fact]
    public async Task CanCallAddPlayerAsync()
    {
      // Arrange
      var player = new Player("TestValue563824593");

      // Act
      await _testClass.AddPlayerAsync(player);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CannotCallAddPlayerAsyncWithNullPlayer()
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.AddPlayerAsync(default(Player)));
    }

    [Fact]
    public async Task CanCallCreatePlayerAsync()
    {
      // Arrange
      var player = new Player("TestValue1603979705");

      // Act
      var result = await _testClass.CreatePlayerAsync(player);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CannotCallCreatePlayerAsyncWithNullPlayer()
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.CreatePlayerAsync(default(Player)));
    }

    [Fact]
    public async Task CanCallUpdatePlayerAsync()
    {
      // Arrange
      var player = new Player("TestValue1379809263");

      // Act
      await _testClass.UpdatePlayerAsync(player);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CannotCallUpdatePlayerAsyncWithNullPlayer()
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.UpdatePlayerAsync(default(Player)));
    }

    [Fact]
    public async Task CanCallDeletePlayerAsync()
    {
      // Arrange
      var player = new Player("TestValue1251034601");

      // Act
      await _testClass.DeletePlayerAsync(player);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CannotCallDeletePlayerAsyncWithNullPlayer()
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.DeletePlayerAsync(default(Player)));
    }
  }
}