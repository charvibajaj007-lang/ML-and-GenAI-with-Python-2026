{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMYKTe8V7BTZd+RAtPJ7N4Q",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/charvibajaj007-lang/ML-and-GenAI-with-Python-2026/blob/main/Assignments/Assignment_3/CharviBajaj_04701012025/Assignment3_CharviBajaj04701012025.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "nfywGttYH7w2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d6667738-5a81-4c08-e92f-3f5708c6c371"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n"
          ]
        }
      ],
      "source": [
        "#function to print first 10 natural numbers\n",
        "def print_num():\n",
        "   for i in range (1,11):\n",
        "     print(i)\n",
        "print_num()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#sum of first n natural numbers\n",
        "\n",
        "def sum_num(n):\n",
        "  sum=0\n",
        "  for i in range (1,n+1):\n",
        "    sum+=i\n",
        "  return sum\n",
        "print(sum_num(10))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q_p9pxNAL0UF",
        "outputId": "66c2e336-3bb3-4812-e156-116311ef09ca"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "55\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# reverse a number\n",
        "def reverse_num(num):\n",
        "    return int(str(num)[::-1])\n",
        "\n",
        "print(reverse_num(12345))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jkecdnzLnxVA",
        "outputId": "98694bbd-6da4-49ce-a9e8-c14ab4d123e9"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "54321\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# count digits in number\n",
        "def count_digits(num):\n",
        "    count = 0\n",
        "    if num == 0:\n",
        "        return 1\n",
        "    while num > 0:\n",
        "        count += 1\n",
        "        num = num // 10\n",
        "    return count\n",
        "\n",
        "print(count_digits(98765))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zaO00zRPpTQS",
        "outputId": "2b5e5163-b143-46a5-c8cb-bf8cf85a6cc4"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#check palindrome\n",
        "def is_palindrome(num):\n",
        "    original = num\n",
        "    rev = 0\n",
        "    while num > 0:\n",
        "        rev = (rev * 10) + (num % 10)\n",
        "        num = num // 10\n",
        "    return original == rev\n",
        "\n",
        "print(is_palindrome(121))"
      ],
      "metadata": {
        "id": "yjDHfAJ8qRtx",
        "outputId": "c85a378c-b7a1-4959-d3e9-db3863028e4e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#generate Fibonacci\n",
        "def fibonacci(n):\n",
        "    a, b = 0, 1\n",
        "    for i in range(n):\n",
        "        print(a)\n",
        "        a, b = b, a + b\n",
        "\n",
        "fibonacci(10)"
      ],
      "metadata": {
        "id": "wdEkQf-gqgA_",
        "outputId": "9993be83-3ec8-41bd-9566-00457c00160d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "1\n",
            "2\n",
            "3\n",
            "5\n",
            "8\n",
            "13\n",
            "21\n",
            "34\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#calculator\n",
        "def add(a, b):\n",
        "  return a + b\n",
        "def sub(a, b):\n",
        "  return a - b\n",
        "def mul(a, b):\n",
        "  return a * b\n",
        "def div(a, b):\n",
        "  return a / b\n",
        "\n",
        "print(\"Add:\", add(10, 5))\n",
        "print(\"Divide:\", div(10, 5))\n",
        "print(\"Multiply:\",mul(10,5))\n",
        "print(\"Subtract:\",sub(10,5))"
      ],
      "metadata": {
        "id": "jB7FCs0nqnIl",
        "outputId": "4047e0b1-ab1e-49ef-bf62-1d299092d9d3",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Add: 15\n",
            "Divide: 2.0\n",
            "Multiply: 50\n",
            "Subtract: 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#create a text file and enter student details\n",
        "def save_file():\n",
        "    file = open(\"students.txt\", \"w\")\n",
        "    file.write(\"Charvi:95, Aanya:94\")\n",
        "    file.close()\n",
        "\n",
        "save_file()"
      ],
      "metadata": {
        "id": "G_22T96brCJ8"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# read data from file\n",
        "def read_file():\n",
        "    file = open(\"students.txt\", \"r\")\n",
        "    print(file.read())\n",
        "    file.close()\n",
        "\n",
        "read_file()"
      ],
      "metadata": {
        "id": "P4XsLfiZreB4",
        "outputId": "d1ae3802-d7ce-44f2-d734-911efced9b16",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Charvi:95, Aanya:94\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Handle division by zero\n",
        "try:\n",
        "    a = int(input(\"Enter numerator: \"))\n",
        "    b = int(input(\"Enter denominator: \"))\n",
        "    print(a / b)\n",
        "except ZeroDivisionError:\n",
        "    print(\"Cannot divide by zero!\")"
      ],
      "metadata": {
        "id": "4EwpUE_WrirJ",
        "outputId": "20cc06ab-9d40-4b1b-d3ef-11f5713dba31",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter numerator: 50\n",
            "Enter denominator: 5\n",
            "10.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# create student class with name and marks\n",
        "class Student:\n",
        "    def __init__(self, name, marks):\n",
        "        self.name = name\n",
        "        self.marks = marks\n",
        "\n",
        "    def display(self):\n",
        "        print(\"Name:\", self.name)\n",
        "        print(\"Marks:\", self.marks)\n",
        "\n",
        "s1 = Student(\"Charvi\", 95)\n",
        "s1.display()"
      ],
      "metadata": {
        "id": "tbxj3BdqrzVC",
        "outputId": "353d1e33-c2a1-4c2e-d213-34aab47417fb",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Name: Charvi\n",
            "Marks: 95\n"
          ]
        }
      ]
    }
  ]
}