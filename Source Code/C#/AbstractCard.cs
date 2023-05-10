using System;
using System.Collections.Generic;

public class AbstractCard {
	public AbstractCard(Card c) {
		Cards = new List<Card>();
		Value = c.face;
		Cards.Add (c);
	}

	private AbstractCard() {}

	public static int SumValues (params AbstractCard[] cards) {
		int sum = 0;
		foreach(AbstractCard card in cards)
			sum += (int)card.Value;
		return sum;
	}

	public bool canAddTo (Player player, params AbstractCard[] cards) {
		if ((int)this.Value + SumValues(cards) > (int)MaxValue)
			return false;
		return !isPaired;
	}

	public void addTo (Player player, params AbstractCard[] others) {
		if (!canAddTo(player, others))
			throw new System.Exception ("Illegal card addition!");
		this.Value = (Card.Face)(this.Value) + SumValues(others);
		foreach (AbstractCard card in others)
			Cards.AddRange(card.Cards);
		this.BuiltBy = player;
	}

	public bool canPairWith (Player player, params AbstractCard[] others) {
		if (!player.hasCard(this.Value))
			return false;
		if (!isPaired && (int)Value > (int)MaxValue)
			return false;
		foreach (AbstractCard card in others) {
			if (isPaired && (int)Value == (int)card.Value)
				return true;
		}
		return false;
	}

	public void pairWith (Player player, params AbstractCard[] cards) {
		if(!canPairWith(player, cards))
			throw new System.Exception ("Illegal card pairing!");
		foreach (AbstractCard card in cards)
			Cards.AddRange(card.Cards);
		this.BuiltBy = player;
		this.isPaired = true;
	}

	public Player BuiltBy {get; private set;}
	public List<Card> Cards {get; private set;}
	public Card.Face Value {get; private set;}
	private bool isPaired = false;
	private static Card.Face MaxValue = (Card.Face)10;
}
