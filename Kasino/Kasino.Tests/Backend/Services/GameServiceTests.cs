namespace Kasino.Tests.Services
{
  using System;
  using System.Collections.Generic;
  using System.Threading.Tasks;
  using Kasino.Models;
  using Kasino.Repositories;
  using Kasino.Services;
  using NSubstitute;
  using Xunit;

  public class GameServiceTests
  {
    private GameService _testClass;
    private IGameRepository _gameRepository;

    public GameServiceTests()
    {
      _gameRepository = Substitute.For<IGameRepository>();
      _testClass = new GameService(_gameRepository);
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new GameService(_gameRepository);

      // Assert
      Assert.NotNull(instance);
    }

    [Fact]
    public void CannotConstructWithNullGameRepository()
    {
      Assert.Throws<ArgumentNullException>(() => new GameService(default(IGameRepository)));
    }

    [Fact]
    public async Task CanCallGetAllGamesAsync()
    {
      // Arrange
      _gameRepository.GetAllGamesAsync().Returns(new[] { new Game(), new Game(), new Game() });

      // Act
      var result = await _testClass.GetAllGamesAsync();

      // Assert
      await _gameRepository.Received().GetAllGamesAsync();

      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CanCallGetGameByIdAsync()
    {
      // Arrange
      var id = "TestValue1858826764";

      _gameRepository.GetGameByIdAsync(Arg.Any<string>()).Returns(new Game());

      // Act
      var result = await _testClass.GetGameByIdAsync(id);

      // Assert
      await _gameRepository.Received().GetGameByIdAsync(Arg.Any<string>());

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
      var id = "TestValue1604646435";

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
      await _gameRepository.Received().CreateGameAsync(Arg.Any<Game>());

      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CannotCallCreateGameAsyncWithNullGame()
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.CreateGameAsync(default(Game)));
    }
  }
}