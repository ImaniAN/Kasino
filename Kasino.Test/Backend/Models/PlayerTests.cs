namespace Kasino.Tests.Models
{
  using System;
  using System.Collections.Generic;
  using Kasino.Models;
  using Xunit;

  public class PlayerTests
  {
    private Player _testClass;
    private string _name;
    private int _score;

    public PlayerTests()
    {
      _name = "TestValue587429005";
      _score = 1330667201;
      _testClass = new Player(_name, _score);
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new Player(_name);

      // Assert
      Assert.NotNull(instance);

      // Act
      instance = new Player(_name, _score);

      // Assert
      Assert.NotNull(instance);
    }

    [Theory]
    [InlineData(null)]
    [InlineData("")]
    [InlineData("   ")]
    public void CannotConstructWithInvalidName(string value)
    {
      Assert.Throws<ArgumentNullException>(() => new Player(value));
      Assert.Throws<ArgumentNullException>(() => new Player(value, _score));
    }

    [Fact]
    public void CanSetAndGetId()
    {
      // Arrange
      var testValue = "TestValue489032400";

      // Act
      _testClass.Id = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.Id);
    }

    [Fact]
    public void NameIsInitializedCorrectly()
    {
      _testClass = new Player(_name);
      Assert.Equal(_name, _testClass.Name);
      _testClass = new Player(_name, _score);
      Assert.Equal(_name, _testClass.Name);
    }

    [Fact]
    public void CanSetAndGetName()
    {
      // Arrange
      var testValue = "TestValue1705955571";

      // Act
      _testClass.Name = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.Name);
    }

    [Fact]
    public void CanSetAndGetHand()
    {
      // Arrange
      var testValue = new List<Card>();

      // Act
      _testClass.Hand = testValue;

      // Assert
      Assert.Same(testValue, _testClass.Hand);
    }

    [Fact]
    public void CanSetAndGetCapturedCards()
    {
      // Arrange
      var testValue = new List<Card>();

      // Act
      _testClass.CapturedCards = testValue;

      // Assert
      Assert.Same(testValue, _testClass.CapturedCards);
    }

    [Fact]
    public void ScoreIsInitializedCorrectly()
    {
      Assert.Equal(_score, _testClass.Score);
    }

    [Fact]
    public void CanSetAndGetScore()
    {
      // Arrange
      var testValue = 1216637687;

      // Act
      _testClass.Score = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.Score);
    }
  }
}