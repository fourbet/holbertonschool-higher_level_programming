#include "lists.h"
#include <stdio.h>
/**
 * insert_node - inserts a number into a sorted linked list
 *
 * @head: pointer to a pointer to a listint_t
 * @number: int to insert
 *
 * Return: the adress of the new node or NULLif failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *previous;
	listint_t *new;
	int count;

	current = *head;
	previous = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	while (current)
	{
		if (current->n > number && count == 0)
		{
			new->next = current;
			*head = new;
			return (new);
		}
		else if (current->n > number)
		{
			new->next = current;
			previous->next = new;
			return (new);
		}
		count++;
		previous = current;
		current = current->next;
	}
	previous->next = new;
	new->next = NULL;
	return (new);
}
