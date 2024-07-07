namespace Kasino.Tests.Backend.Helpers
{
  using System;
  using Kasino.Backend.Helpers;
  using Xunit;

  public class MappingProfileTests
  {
    private MappingProfile _testClass;

    public MappingProfileTests()
    {
      _testClass = new MappingProfile();
    }

    [Fact]
    public void CanConstruct()
    {
      // Act
      var instance = new MappingProfile();

      // Assert
      Assert.NotNull(instance);
    }
  }
}