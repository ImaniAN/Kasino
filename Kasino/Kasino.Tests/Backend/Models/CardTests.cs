namespace Kasino.Tests.Models
{
  using System;
  using Kasino.Models;
  using Xunit;

  public class CardTests
  {
    private Card _testClass;
    private int _id;
    private Suits _suit;
    private int _value;

    public CardTests()
    {
      _id = 931564827;
      _suit = Suits.S;
      _value = 1769288091;
      _testClass = new Card(_id, _suit, _value);
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new Card(_id, _suit, _value);

      // Assert
      Assert.NotNull(instance);
    }

    [Fact]
    public void CanCallIsSpecialCard()
    {
      // Act
      var result = _testClass.IsSpecialCard();

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public void CanCallPointValue()
    {
      // Act
      var result = _testClass.PointValue();

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Fact]
    public void IdIsInitializedCorrectly()
    {
      Assert.Equal(_id, _testClass.Id);
    }

    [Fact]
    public void CanSetAndGetId()
    {
      // Arrange
      var testValue = 192152471;

      // Act
      _testClass.Id = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.Id);
    }

    [Fact]
    public void SuitIsInitializedCorrectly()
    {
      Assert.Equal(_suit, _testClass.Suit);
    }

    [Fact]
    public void CanSetAndGetSuit()
    {
      // Arrange
      var testValue = Suits.D;

      // Act
      _testClass.Suit = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.Suit);
    }

    [Fact]
    public void ValueIsInitializedCorrectly()
    {
      Assert.Equal(_value, _testClass.Value);
    }

    [Fact]
    public void CanSetAndGetValue()
    {
      // Arrange
      var testValue = 1605614647;

      // Act
      _testClass.Value = testValue;

      // Assert
      Assert.Equal(testValue, _testClass.Value);
    }
  }
}