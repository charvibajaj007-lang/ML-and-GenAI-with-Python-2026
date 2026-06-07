{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOMOOADQv/YSXT2jk15yjDP",
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
        "<a href=\"https://colab.research.google.com/github/charvibajaj007-lang/ML-and-GenAI-with-Python-2026/blob/main/Assignment3_CharviBajaj04701012025.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
      "execution_count": null,
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
        "id": "jkecdnzLnxVA"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}