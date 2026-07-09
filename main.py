from app.workflows.movie_workflow import MovieWorkflow


def main():

    workflow = MovieWorkflow()

    workflow.run(
        genre="Romance",
        language="English",
        duration=10
    )


if __name__ == "__main__":
    main()