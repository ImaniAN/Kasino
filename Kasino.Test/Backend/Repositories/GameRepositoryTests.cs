namespace Kasino.Tests.Repositories
{
  using System;
  using System.Threading.Tasks;
  using Kasino.Data;
  using Kasino.Models;
  using Kasino.Repositories;
  using Xunit;

  public class GameRepositoryTests
  {
    private GameRepository _testClass;
    private GameDbContext _context;

    public GameRepositoryTests()
    {
      _context = new GameDbContext(new DbContextOptions<GameDbContext>());
      _testClass = new GameRepository(_context);
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new GameRepository(_context);

      // Assert
      Assert.NotNull(instance);
    }

    [Fact]
    public void CannotConstructWithNullContext()
    {
      Assert.Throws<ArgumentNullException>(() => new GameRepository(default(GameDbContext)));
    }

    [Fact]
    public async Task CanCallGetAllGamesAsync()
    {
      // Act
      var result = await _testClass.GetAllGamesAsync();

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CanCallGetGameByIdAsync()
    {
      // Arrange
      var id = "TestValue1726424225";

      // Act
      var result = await _testClass.GetGameByIdAsync(id);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Theory]
    [InlineData(null)]
    [InlineData("")]
    [InlineData("   ")]
    public async Task CannotCallGetGameByIdAsyncWithInvalidId(string value)
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.GetGameByIdAsync(value));
    }

    [Fact]
    public async Task GetGameByIdAsyncPerformsMapping()
    {
      // Arrange
      var id = "TestValue758775879";

      // Act
      var result = await _testClass.GetGameByIdAsync(id);

      // Assert
      Assert.Same(id, result.Id);
    }

    [Fact]
    public async Task CanCallCreateGameAsync()
    {
      // Arrange
      var game = new Game();

      // Act
      await _testClass.CreateGameAsync(game);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CannotCallCreateGameAsyncWithNullGame()
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.CreateGameAsync(default(Game)));
    }
  }
}