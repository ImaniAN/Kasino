namespace Kasino.Tests.Controllers
{
  using System;
  using System.Collections.Generic;
  using System.Threading.Tasks;
  using Kasino.Controllers;
  using Kasino.Models;
  using Kasino.Services;
  using NSubstitute;
  using Xunit;

  public class PlayerControllerTests
  {
    private PlayerController _testClass;
    private IPlayerService _playerService;

    public PlayerControllerTests()
    {
      _playerService = Substitute.For<IPlayerService>();
      _testClass = new PlayerController(_playerService);
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new PlayerController(_playerService);

      // Assert
      Assert.NotNull(instance);
    }

    [Fact]
    public void CannotConstructWithNullPlayerService()
    {
      Assert.Throws<ArgumentNullException>(() => new PlayerController(default(IPlayerService)));
    }

    [Fact]
    public async Task CanCallGetPlayers()
    {
      // Arrange
      _playerService.GetAllPlayersAsync().Returns(new[] { new Player("TestValue1525959889"), new Player("TestValue1149848750"), new Player("TestValue150798042") });

      // Act
      var result = await _testClass.GetPlayers();

      // Assert
      await _playerService.Received().GetAllPlayersAsync();

      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CanCallGetPlayer()
    {
      // Arrange
      var id = "TestValue348318637";

      _playerService.GetPlayerByIdAsync(Arg.Any<string>()).Returns(new Player("TestValue1434580581"));

      // Act
      var result = await _testClass.GetPlayer(id);

      // Assert
      await _playerService.Received().GetPlayerByIdAsync(Arg.Any<string>());

      throw new NotImplementedException("Create or modify test");
    }

    [Theory]
    [InlineData(null)]
    [InlineData("")]
    [InlineData("   ")]
    public async Task CannotCallGetPlayerWithInvalidId(string value)
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.GetPlayer(value));
    }

    [Fact]
    public async Task CanCallCreatePlayer()
    {
      // Arrange
      var player = new Player("TestValue533265229");

      _playerService.CreatePlayerAsync(Arg.Any<Player>()).Returns(new Player("TestValue635029482"));

      // Act
      var result = await _testClass.CreatePlayer(player);

      // Assert
      await _playerService.Received().CreatePlayerAsync(Arg.Any<Player>());

      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public async Task CannotCallCreatePlayerWithNullPlayer()
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.CreatePlayer(default(Player)));
    }
  }
}