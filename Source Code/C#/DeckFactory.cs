using System.Collections.Generic;
using System;

public abstract class DeckFactory {
	public static List<Card> createDeck() {
		List<Card> deck = new List<Card>();
		foreach (Card.Suit suit in Enum.GetValues(typeof(Card.Suit))) {
			for (Card.Face face = Card.Face.ACE; face <= Card.Face.KING; ++face) {
				deck.Add (new Card(face, suit));
			}
		}
		return deck;
	}
}
