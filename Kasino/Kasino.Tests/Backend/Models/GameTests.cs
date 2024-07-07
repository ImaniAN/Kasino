namespace Kasino.Tests.Models
{
  using System;
  using System.Collections.Generic;
  using Kasino.Backend.Models;
  using Kasino.Models;
  using Xunit;

  public class GameTests
  {
    private Game _testClass;

    public GameTests()
    {
      _testClass = new Game();
    }

    [Fact]
    public void CanCallAddBuildToGameState()
    {
      // Arrange
      var build = new Build(new List<Card>());

      // Act
      _testClass.AddBuildToGameState(build);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public void CannotCallAddBuildToGameStateWithNullBuild()
    {
      Assert.Throws<ArgumentNullException>(() => _testClass.AddBuildToGameState(default(Build)));
    }

    [Fact]
    public void CanCallIsCardSpecial()
    {
      // Arrange
      var card = new Card(1300355227, Suits.H, 1128185322);

      // Act
      var result = Game.IsCardSpecial(card);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public void CannotCallIsCardSpecialWithNullCard()
    {
      Assert.Throws<ArgumentNullException>(() => Game.IsCardSpecial(default(Card)));
    }

    [Fact]
    public void CanCallDealCards()
    {
      // Act
      _testClass.DealCards();

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public void CanCallCapture()
    {
      // Arrange
      var playedCard = new Card(1878231763, Suits.H, 149095082);
      var player = new Player("TestValue54041068");

      // Act
      _testClass.Capture(playedCard, player);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public void CannotCallCaptureWithNullPlayedCard()
    {
      Assert.Throws<ArgumentNullException>(() => _testClass.Capture(default(Card), new Player("TestValue396155918")));
    }

    [Fact]
    public void CannotCallCaptureWithNullPlayer()
    {
      Assert.Throws<ArgumentNullException>(() => _testClass.Capture(new Card(1276628551, Suits.S, 1071489977), default(Player)));
    }

    [Fact]
    public void CanCallBuild()
    {
      // Arrange
      var playedCard = new Card(2083434240, Suits.D, 1603105484);
      var player = new Player("TestValue600475285");
      var targetValue = 1857238588;

      // Act
      _testClass.Build(playedCard, player, targetValue);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public void CannotCallBuildWithNullPlayedCard()
    {
      Assert.Throws<ArgumentNullException>(() => _testClass.Build(default(Card), new Player("TestValue51431735"), 1467568031));
    }

    [Fact]
    public void CannotCallBuildWithNullPlayer()
    {
      Assert.Throws<ArgumentNullException>(() => _testClass.Build(new Card(1014629352, Suits.S, 2094949203), default(Player), 811322827));
    }

    [Fact]
    public void CanCallLahla()
    {
      // Arrange
      var playedCard = new Card(1049479779, Suits.D, 1764298090);
      var player = new Player("TestValue1057156131");

      // Act
      _testClass.Lahla(playedCard, player);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public void CannotCallLahlaWithNullPlayedCard()
    {
      Assert.Throws<ArgumentNullException>(() => _testClass.Lahla(default(Card), new Player("TestValue1537802850")));
    }

    [Fact]
    public void CannotCallLahlaWithNullPlayer()
    {
      Assert.Throws<ArgumentNullException>(() => _testClass.Lahla(new Card(451277501, Suits.C, 690178670), default(Player)));
    }

    [Fact]
    public void CanCallCalculateScores()
    {
      // Act
      _testClass.CalculateScores();

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public void CanSetAndGetId()
    {
      // Arrange
      var testValue = "TestValue1939771700";

      // Act
      _testClass.Id = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.Id);
    }

    [Fact]
    public void CanSetAndGetPlayers()
    {
      // Arrange
      var testValue = new List<Player>();

      // Act
      _testClass.Players = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Players);
    }

    [Fact]
    public void CanSetAndGetFloorCards()
    {
      // Arrange
      var testValue = new List<Card>();

      // Act
      _testClass.FloorCards = testValue;

      // Assert
      Assert.Same(testValue, _testClass.FloorCards);
    }

    [Fact]
    public void CanSetAndGetDeck()
    {
      // Arrange
      var testValue = new Deck();

      // Act
      _testClass.Deck = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Deck);
    }

    [Fact]
    public void CanSetAndGetCurrentRound()
    {
      // Arrange
      var testValue = 2016340261;

      // Act
      _testClass.CurrentRound = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.CurrentRound);
    }

    [Fact]
    public void CanSetAndGetBuilds()
    {
      // Arrange
      var testValue = new List<Build>();

      // Act
      _testClass.Builds = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Builds);
    }
  }
}