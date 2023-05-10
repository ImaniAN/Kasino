using System;
using System.Collections.Generic;

public abstract class Player {
	public Player () {
		Counter = new CardCounter();
	}

	public bool hasCard (Card.Face face) {
		foreach(Card c in hand) {
			if (c.face == face)
				return true;
		}
		return false;
	}

	public abstract void makeMove (GameData game);

	public CardCounter Counter {get; private set;}
	private List<Card> hand;
}
