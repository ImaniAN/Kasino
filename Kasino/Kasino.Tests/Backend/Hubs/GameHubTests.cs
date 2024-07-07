namespace Kasino.Tests.Hubs
{
  using System;
  using System.Threading.Tasks;
  using Kasino.Hubs;
  using Xunit;

  public class GameHubTests
  {
    private GameHub _testClass;

    public GameHubTests()
    {
      _testClass = new GameHub();
    }

    [Fact]
    public async Task CanCallSendMessage()
    {
      // Arrange
      var user = "TestValue1315369588";
      var message = "TestValue730060632";

      // Act
      await _testClass.SendMessage(user, message);

      // Assert
      throw new NotImplementedException("Create or modify test");
    }

    [Theory]
    [InlineData(null)]
    [InlineData("")]
    [InlineData("   ")]
    public async Task CannotCallSendMessageWithInvalidUser(string value)
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.SendMessage(value, "TestValue1897055068"));
    }

    [Theory]
    [InlineData(null)]
    [InlineData("")]
    [InlineData("   ")]
    public async Task CannotCallSendMessageWithInvalidMessage(string value)
    {
      await Assert.ThrowsAsync<ArgumentNullException>(() => _testClass.SendMessage("TestValue319527022", value));
    }
  }
}