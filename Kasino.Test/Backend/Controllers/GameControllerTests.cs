namespace Kasino.Tests.Controllers
{
  using System;
  using System.Threading.Tasks;
  using Kasino.Backend.Services;
  using Kasino.Controllers;
  using Kasino.Models;
  using NSubstitute;
  using Xunit;

  public class GameControllerTests
  {
    private GameController _testClass;
    private IGameService _gameService;

    public GameControllerTests()
    {
      _gameService = Substitute.For<IGameService>();
      _testClass = new GameController(_gameService);
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new GameController(_gameService);

      // Assert
      Assert.NotNull(instance);
    }

    [Fact]
    public void CannotConstructWithNullGameService()
    {
      Assert.Throws<ArgumentNullException>(() => new GameController(default(IGameService)));
    }

    [Fact]
    public async Task CanCallGetGamesAsync()
    {
      // Arrange
      _gameService.GetAllGamesAsync().Returns(new object());

      // Act
      var result = await _testClass.GetGamesAsync();

      // Assert
      await _gameService.Received().GetAllGamesAsync();

      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CanCallGetGameAsync()
    {
      // Arrange
      var id = "TestValue1443176283";

      _gameService.GetGameByIdAsync(Arg.Any<string>()).Returns(new Game());

      // Act
      var result = await _testClass.GetGameAsync(id);

      // Assert
      await _gameService.Received().GetGameByIdAsync(Arg.Any<string>());

      throw new NotImplementedException("Create or modify test");
    }

    [Theory]
    [InlineData(null)]
    [InlineData("")]
    [InlineData("   ")]
    public async Task CannotCallGetGameAsyncWithInvalidId(string value)
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.GetGameAsync(value));
    }

    [Fact]
    public async Task CanCallCreateGameAsync()
    {
      // Arrange
      var game = new Game();

      // Act
      var result = await _testClass.CreateGameAsync(game);

      // Assert
      await _gameService.Received().CreateGameAsync(Arg.Any<Game>());

      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CannotCallCreateGameAsyncWithNullGame()
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.CreateGameAsync(default(Game)));
    }
  }
}