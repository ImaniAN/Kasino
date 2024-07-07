namespace Kasino.Tests.Backend.DTOs
{
  using System;
  using System.Collections.Generic;
  using Kasino.Backend.DTOs;
  using Xunit;

  public class GameDtoTests
  {
    private GameDto _testClass;

    public GameDtoTests()
    {
      _testClass = new GameDto();
    }

    [Fact]
    public void CanSetAndGetId()
    {
      // Arrange
      var testValue = "TestValue1680791384";

      // Act
      _testClass.Id = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.Id);
    }

    [Fact]
    public void CanSetAndGetName()
    {
      // Arrange
      var testValue = "TestValue90559287";

      // Act
      _testClass.Name = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.Name);
    }

    [Fact]
    public void CanSetAndGetGenre()
    {
      // Arrange
      var testValue = "TestValue1301953679";

      // Act
      _testClass.Genre = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.Genre);
    }

    [Fact]
    public void CanSetAndGetReleaseDate()
    {
      // Arrange
      var testValue = DateTime.UtcNow;

      // Act
      _testClass.ReleaseDate = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.ReleaseDate);
    }
  }

  public class PlayerDtoTests
  {
    private PlayerDto _testClass;
    private string _playerIdString;
    private string _nameString;
    private int _scoreInt32;
    private List<GameDto> _games;
    private string _playerIdString;
    private string _nameString;
    private int _scoreInt32;

    public PlayerDtoTests()
    {
      _playerIdString = "TestValue754032896";
      _nameString = "TestValue379996732";
      _scoreInt32 = 759566375;
      _games = new List<GameDto>();
      _playerIdString = "TestValue1382235235";
      _nameString = "TestValue2074030257";
      _scoreInt32 = 775328490;
      _testClass = new PlayerDto(_playerIdString, _nameString, _scoreInt32, _games);
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new PlayerDto(_playerIdString, _nameString, _scoreInt32, _games);

      // Assert
      Assert.NotNull(instance);
    }

    [Fact]
    public void ImplementsIEquatable_PlayerDto()
    {
      // Arrange
      var same = new PlayerDto(_playerIdString, _nameString, _scoreInt32, _games);
      var different = new PlayerDto("TestValue1028199962", "TestValue1184830472", 2067828889);

      // Assert
      Assert.False(_testClass.Equals(default(object)));
      Assert.False(_testClass.Equals(new object()));
      Assert.True(_testClass.Equals((object)same));
      Assert.False(_testClass.Equals((object)different));
      Assert.True(_testClass.Equals(same));
      Assert.False(_testClass.Equals(different));
      Assert.Equal(same.GetHashCode(), _testClass.GetHashCode());
      Assert.NotEqual(different.GetHashCode(), _testClass.GetHashCode());
      Assert.True(_testClass == same);
      Assert.False(_testClass == different);
      Assert.False(_testClass != same);
      Assert.True(_testClass != different);
    }

    [Fact]
    public void GamesIsInitializedCorrectly()
    {
      Assert.Same(_games, _testClass.Games);
    }

    [Fact]
    public void CanSetAndGetGames()
    {
      // Arrange
      var testValue = new List<GameDto>();

      // Act
      _testClass.Games = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Games);
    }

    [Fact]
    public void PlayerIdIsInitializedCorrectly()
    {
      _testClass = new PlayerDto(_playerIdString, _nameString, _scoreInt32, _games);
      Assert.Equal(_playerIdString, _testClass.PlayerId);
      _testClass = new PlayerDto(_playerIdString, _nameString, _scoreInt32);
      Assert.Equal(_playerIdString, _testClass.PlayerId);
    }

    [Fact]
    public void NameIsInitializedCorrectly()
    {
      _testClass = new PlayerDto(_playerIdString, _nameString, _scoreInt32, _games);
      Assert.Equal(_nameString, _testClass.Name);
      _testClass = new PlayerDto(_playerIdString, _nameString, _scoreInt32);
      Assert.Equal(_nameString, _testClass.Name);
    }

    [Fact]
    public void ScoreIsInitializedCorrectly()
    {
      _testClass = new PlayerDto(_playerIdString, _nameString, _scoreInt32, _games);
      Assert.Equal(_scoreInt32, _testClass.Score);
      _testClass = new PlayerDto(_playerIdString, _nameString, _scoreInt32);
      Assert.Equal(_scoreInt32, _testClass.Score);
    }
  }
}