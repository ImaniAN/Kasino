namespace Kasino.Tests.Models
{
  using System;
  using System.Collections.Generic;
  using Kasino.Models;
  using Xunit;

  public class MoveTests
  {
    private Move _testClass;
    private Player _player;
    private Card _playedCard;
    private Move.MoveActionType _actionType;
    private List<Card> _targetCards;
    private int _targetValue;

    public MoveTests()
    {
      _player = new Player("TestValue477429325");
      _playedCard = new Card(947880781, Suits.D, 1303286235);
      _actionType = Move.MoveActionType.Build;
      _targetCards = new List<Card>();
      _targetValue = 1301057906;
      _testClass = new Move(_player, _playedCard, _actionType, _targetCards);
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new Move(_player, _playedCard, _actionType);

      // Assert
      Assert.NotNull(instance);

      // Act
      instance = new Move(_player, _playedCard, _actionType, _targetCards);

      // Assert
      Assert.NotNull(instance);

      // Act
      instance = new Move(_player, _playedCard, _actionType, _targetValue);

      // Assert
      Assert.NotNull(instance);
    }

    [Fact]
    public void CannotConstructWithNullPlayer()
    {
      Assert.Throws<ArgumentNullException>(() => new Move(default(Player), _playedCard, _actionType));
      Assert.Throws<ArgumentNullException>(() => new Move(default(Player), _playedCard, _actionType, _targetCards));
      Assert.Throws<ArgumentNullException>(() => new Move(default(Player), _playedCard, _actionType, _targetValue));
    }

    [Fact]
    public void CannotConstructWithNullPlayedCard()
    {
      Assert.Throws<ArgumentNullException>(() => new Move(_player, default(Card), _actionType));
      Assert.Throws<ArgumentNullException>(() => new Move(_player, default(Card), _actionType, _targetCards));
      Assert.Throws<ArgumentNullException>(() => new Move(_player, default(Card), _actionType, _targetValue));
    }

    [Fact]
    public void CannotConstructWithNullTargetCards()
    {
      Assert.Throws<ArgumentNullException>(() => new Move(_player, _playedCard, _actionType, default(List<Card>)));
    }

    [Fact]
    public void PlayerIsInitializedCorrectly()
    {
      _testClass = new Move(_player, _playedCard, _actionType);
      Assert.Same(_player, _testClass.Player);
      _testClass = new Move(_player, _playedCard, _actionType, _targetCards);
      Assert.Same(_player, _testClass.Player);
      _testClass = new Move(_player, _playedCard, _actionType, _targetValue);
      Assert.Same(_player, _testClass.Player);
    }

    [Fact]
    public void CanSetAndGetPlayer()
    {
      // Arrange
      var testValue = new Player("TestValue1934860651");

      // Act
      _testClass.Player = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Player);
    }

    [Fact]
    public void PlayedCardIsInitializedCorrectly()
    {
      _testClass = new Move(_player, _playedCard, _actionType);
      Assert.Same(_playedCard, _testClass.PlayedCard);
      _testClass = new Move(_player, _playedCard, _actionType, _targetCards);
      Assert.Same(_playedCard, _testClass.PlayedCard);
      _testClass = new Move(_player, _playedCard, _actionType, _targetValue);
      Assert.Same(_playedCard, _testClass.PlayedCard);
    }

    [Fact]
    public void CanSetAndGetPlayedCard()
    {
      // Arrange
      var testValue = new Card(1610320736, Suits.D, 1187706701);

      // Act
      _testClass.PlayedCard = testValue;

      // Assert
      Assert.Same(testValue, _testClass.PlayedCard);
    }

    [Fact]
    public void ActionTypeIsInitializedCorrectly()
    {
      _testClass = new Move(_player, _playedCard, _actionType);
      Assert.Equal(_actionType, _testClass.ActionType);
      _testClass = new Move(_player, _playedCard, _actionType, _targetCards);
      Assert.Equal(_actionType, _testClass.ActionType);
      _testClass = new Move(_player, _playedCard, _actionType, _targetValue);
      Assert.Equal(_actionType, _testClass.ActionType);
    }

    [Fact]
    public void CanSetAndGetActionType()
    {
      // Arrange
      var testValue = Move.MoveActionType.Capture;

      // Act
      _testClass.ActionType = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.ActionType);
    }

    [Fact]
    public void TargetCardsIsInitializedCorrectly()
    {
      Assert.Same(_targetCards, _testClass.TargetCards);
    }

    [Fact]
    public void CanSetAndGetTargetCards()
    {
      // Arrange
      var testValue = new List<Card>();

      // Act
      _testClass.TargetCards = testValue;

      // Assert
      Assert.Same(testValue, _testClass.TargetCards);
    }

    [Fact]
    public void TargetValueIsInitializedCorrectly()
    {
      _testClass = new Move(_player, _playedCard, _actionType, _targetValue);
      Assert.Equal(_targetValue, _testClass.TargetValue);
    }

    [Fact]
    public void CanSetAndGetTargetValue()
    {
      // Arrange
      var testValue = 987163142;

      // Act
      _testClass.TargetValue = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.TargetValue);
    }

    [Fact]
    public void CanSetAndGetMoveId()
    {
      // Arrange
      var testValue = 496555826;

      // Act
      _testClass.MoveId = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.MoveId);
    }

    [Fact]
    public void CanSetAndGetPlayerId()
    {
      // Arrange
      var testValue = "TestValue1876392014";

      // Act
      _testClass.PlayerId = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.PlayerId);
    }

    [Fact]
    public void CanSetAndGetCardsPlayed()
    {
      // Arrange
      var testValue = new List<Card>();

      // Act
      _testClass.CardsPlayed = testValue;

      // Assert
      Assert.Same(testValue, _testClass.CardsPlayed);
    }

    [Fact]
    public void CanSetAndGetMoveSequence()
    {
      // Arrange
      var testValue = 1745988012;

      // Act
      _testClass.MoveSequence = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.MoveSequence);
    }

    [Fact]
    public void CanSetAndGetPointsGained()
    {
      // Arrange
      var testValue = 1689910570;

      // Act
      _testClass.PointsGained = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.PointsGained);
    }

    [Fact]
    public void CanSetAndGetTimestamp()
    {
      // Arrange
      var testValue = DateTime.UtcNow;

      // Act
      _testClass.Timestamp = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.Timestamp);
    }
  }
}